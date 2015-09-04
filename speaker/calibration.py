'Module for creation and manipulation of speaker calibration curve objects.'


import numpy as np
import csv
from scipy.interpolate import interp1d
from pkg_resources import resource_filename


default_csvfilename = resource_filename(
    __name__, 'calibration_data/line_integral.csv')


class LineIntegral(object):
    '''Line integrated pressure perturbation calibration curve object.

    Attributes:
    -----------
    k - array, (`N`,)
        Wavenumber of speaker's sound wave
        [k] = cm^{-1}

    P - array, (`N`,)
        Line integrated power
        [P] = AU

    curve - interp1d <scipy.interpolate.interpolate.interp1d>
        Calibration curve function that *interpolates* values
        of `P` for arbitrary wavenumber(s) `knew` (subject to the
        constraint that new wavenumber(s) satisfies

                        min(k) <= knew <= max(k)

    '''
    def __init__(self, csvfilename=default_csvfilename,
                 delimiter=',', interp_kind='linear'):
        '''Create line integrated pressure perturbation calibration object.

        Input Parameters:
        -----------------
        csvfilename - string
            The path to the CSV file containing the line integrated
            calibration data. The file's first column should contain
            wavenumber `k` and the second column should contain
            the line integrated power.

        delimiter - string
            The delimiter used in `csvfilename`.

        interp_kind - string
            The calibration data from `csvfilename` will be interpolated
            onto any desired grid. `interp_kind` specifies the kind
            of interpolation to perform.

        '''
        self.loadData(csvfilename, delimiter=delimiter)
        self.curve = self.interpolateData(kind=interp_kind)

    def loadData(self, csvfilename, delimiter=','):
        'Load data from csv file.'
        # Initialize wavenumber `k` and line integrated power `P`
        # as empty lists
        k = []
        P = []

        with open(csvfilename, 'rb') as csvfile:
            reader = csv.reader(csvfile, delimiter=delimiter)

            # First line contains the column titles; this advances the reader
            # to the next row so we can collect the data from the CSV file
            reader.next()

            # Iteratively build up the `k` and `P` arrays
            for row in reader:
                # Note that `row` is a list of *strings*, so we need to
                # convert each entry to a float
                k.append(float(row[0]))
                P.append(float(row[1]))

        # Cast the `k` and `P` arrays as numpy arrays
        self.k = np.asarray(k)
        self.P = np.asarray(P)

        return

    def interpolateData(self, kind='linear'):
        'Create function allowing interpolation of loaded data.'
        return interp1d(self.k, self.P, kind=kind)
