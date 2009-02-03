############################################################################
##
## Copyright (C) 2006-2007 University of Utah. All rights reserved.
##
## This file is part of VisTrails.
##
## This file may be used under the terms of the GNU General Public
## License version 2.0 as published by the Free Software Foundation
## and appearing in the file LICENSE.GPL included in the packaging of
## this file.  Please review the following to ensure GNU General Public
## Licensing requirements will be met:
## http://www.opensource.org/licenses/gpl-license.php
##
## If you are unsure which license is appropriate for your use (for
## instance, you are interested in developing a commercial derivative
## of VisTrails), please contact us at vistrails@sci.utah.edu.
##
## This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
## WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.
##
############################################################################
#  ITK package for VisTrails

version = '0.2'
identifier = 'edu.utah.sci.vistrails.itk'
name = 'ITK'

import core.bundles.utils
import core.requirements
from core.modules.vistrails_module import Module, ModuleError

# Ugly, but Carlos doesnt know any better
if core.bundles.utils.guess_system() == 'linux-ubuntu':
    import sys
    sys.path.append('/usr/local/lib/VisTrailsITK')

try:
    from core.bundles import py_import
    itk = py_import('itk', {'linux-ubuntu': 'vistrails-itk'})
except ImportError:
    raise core.requirements.MissingRequirement("ITK and WrapITK")

import core.modules
import core.modules.module_registry

# ITK Package imports
from PixelType import *
from FeatureExtractionFilters import *
from ITK import *
from Image import Image
from IntensityFilters import *
from SegmentationFilters import *
from SelectionFilters import *
from SmoothingFilters import *
from ImageReader import *

def initialize(*args, **keywords):
    reg = core.modules.module_registry
    basic = core.modules.basic_modules

########################################################################################
# Misc.
    Index2D.register(reg,basic)
    Index3D.register(reg,basic)
    Size.register(reg,basic)
    Region.register(reg,basic)
    PixelType.register(reg,basic)
    Filter.register(reg,basic)

    Image.register(reg,basic)

########################################################################################
# Pixel Types
    pixeltypes = [PixelTypeFloat,
                  PixelTypeUnsignedChar,
                  PixelTypeUnsignedShort,
                  PixelTypeRGB]

    for cls in pixeltypes:
        cls.register(reg,basic)


########################################################################################
# Feature Extraction Filters
    featurefilters = [GradientMagnitudeRecursiveGaussianImageFilter]

    for cls in featurefilters:
        cls.register(reg,basic)

########################################################################################
# Intensity Filters
    intensityfilters = [RescaleIntensityImageFilter,
                        SigmoidImageFilter,
                        ThresholdImageFilter]

    for cls in intensityfilters:
        cls.register(reg,basic)

########################################################################################
# Segmentation Filters
    segmentationfilters = [IsolatedWatershedImageFilter,
                           ConnectedThresholdImageFilter,
                           ConfidenceConnectedImageFilter,
                           IsolatedConnectedImageFilter]

    for cls in segmentationfilters:
        cls.register(reg,basic)

########################################################################################
# Selection Filters
    selectionfilters = [RegionOfInterestImageFilter,
                        CastImageFilter,
                        ExtractImageFilter]

    for cls in selectionfilters:
        cls.register(reg,basic)

########################################################################################
# Smoothing Filters
    smoothingfilters = [CurvatureAnisotropicDiffusionFilter,
                        RecursiveGaussianImageFilter,
                        CurvatureFlowImageFilter]

    for cls in smoothingfilters:
        cls.register(reg,basic)

########################################################################################
# Image Reader
    imagereader = [ImageReader,
                   ImageToFile,
                   GDCMReader,
                   DICOMReader]


    for cls in imagereader:
        cls.register(reg,basic)
