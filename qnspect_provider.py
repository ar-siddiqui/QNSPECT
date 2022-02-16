# -*- coding: utf-8 -*-

"""
/***************************************************************************
 QNSPECT
                                 A QGIS plugin
 QGIS Plugin for NOAA Nonpoint Source Pollution and Erosion Comparison Tool (NSPECT)
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2021-12-29
        copyright            : (C) 2021 by NOAA
        email                : shan dot burkhalter at noaa dot gov
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

__author__ = "Abdul Raheem Siddiqui"
__date__ = "2021-12-29"
__copyright__ = "(C) 2021 by NOAA"

# This will get replaced with a git SHA1 when you do a git archive

__revision__ = "$Format:%H$"

import os
import inspect
from qgis.PyQt.QtGui import QIcon

from qgis.core import QgsProcessingProvider
from QNSPECT.qnspect_algorithm import QNSPECTAlgorithm
from QNSPECT import algorithms


class QNSPECTProvider(QgsProcessingProvider):
    def __init__(self):
        """
        Default constructor.
        """
        QgsProcessingProvider.__init__(self)

    def unload(self):
        """
        Unloads the provider. Any tear-down steps required by the provider
        should be implemented here.
        """
        pass

    def loadAlgorithms(self):
        """
        Loads all algorithms belonging to this provider.
        """

        alg_classes = [
            m[1]
            for m in inspect.getmembers(algorithms, inspect.isclass)
            if issubclass(m[1], QNSPECTAlgorithm)
        ]

        for alg_class in alg_classes:
            self.addAlgorithm(alg_class())

    def id(self):
        """
        Returns the unique provider id, used for identifying the provider. This
        string should be a unique, short, character only string, eg "qgis" or
        "gdal". This string should not be localised.
        """
        return "qnspect"

    def name(self):
        """
        Returns the provider name, which is used to describe the provider
        within the GUI.

        This string should be short and localised.
        """
        return self.tr("QNSPECT")

    def icon(self):
        """
        Should return a QIcon which is used for your provider inside
        the Processing toolbox.
        """
        cmd_folder = os.path.split(inspect.getfile(inspect.currentframe()))[0]
        icon = QIcon(
            os.path.join(os.path.join(cmd_folder, "resources/branding/icon.svg"))
        )
        return icon

    def longName(self):
        """
        Returns the a longer version of the provider name, which can include
        extra details such as version numbers. This string should be localised.
        The default implementation returns the same string as name().
        """
        return self.tr("Nonpoint Source Pollution and Erosion Comparison Tool")
