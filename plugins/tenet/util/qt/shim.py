
#
# this global is used to indicate whether Qt bindings for python are present
# and available for use by Lighthouse.
#

QT_AVAILABLE = False

#------------------------------------------------------------------------------
# PyQt5 <--> PySide2 Compatibility
#------------------------------------------------------------------------------
#
#    we use this file to shim/re-alias a few Qt API's to ensure compatibility
#    between the popular Qt frameworks. these shims serve to reduce the number
#    of compatibility checks in the plugin code that consumes them.
#
#    this file was critical for retaining compatibility with Qt4 frameworks
#    used by IDA 6.8/6.95, but it less important now. support for Qt 4 and
#    older versions of IDA will be deprecated in Lighthouse v0.9.0
#

USING_PYSIDE6 = False
USING_PYQT5 = False
USING_PYSIDE2 = False

# ------------------------------------------------------------------------------
# PySide6 Compatibility (IDA 9.x)
#------------------------------------------------------------------------------

# attempt to load PySide6
if QT_AVAILABLE == False:
    try:
        import PySide6.QtGui as QtGui
        import PySide6.QtCore as QtCore
        import PySide6.QtWidgets as QtWidgets
        
        # On essaie d'importer shiboken6 pour remplacer sip.wrapinstance plus tard si besoin
        try:
            import shiboken6 as shiboken
        except ImportError:
            pass

        # alias for less PySide6 <--> PyQt5 shimming
        QtCore.pyqtSignal = QtCore.Signal
        QtCore.pyqtSlot = QtCore.Slot

        # importing went okay, PySide6 must be available for use
        QT_AVAILABLE = True
        USING_PYSIDE6 = True

    # import failed, PySide6 is not available
    except ImportError:
        pass
print(f"[Tenet] USING_PYSIDE6={USING_PYSIDE6}")

#------------------------------------------------------------------------------
# PyQt5 Compatibility
#------------------------------------------------------------------------------

# attempt to load PyQt5
if QT_AVAILABLE == False:
    try:
        import PyQt5.QtGui as QtGui
        import PyQt5.QtCore as QtCore
        import PyQt5.QtWidgets as QtWidgets
        from PyQt5 import sip

        # importing went okay, PyQt5 must be available for use
        QT_AVAILABLE = True
        USING_PYQT5 = True

    # import failed, PyQt5 is not available
    except ImportError:
        pass
print(f"[Tenet] USING_PYQT5={USING_PYQT5}")

#------------------------------------------------------------------------------
# PySide2 Compatibility
#------------------------------------------------------------------------------

# if PyQt5 did not import, try to load PySide
if QT_AVAILABLE == False:
    try:
        import PySide2.QtGui as QtGui
        import PySide2.QtCore as QtCore
        import PySide2.QtWidgets as QtWidgets

        # alias for less PySide2 <--> PyQt5 shimming
        QtCore.pyqtSignal = QtCore.Signal
        QtCore.pyqtSlot = QtCore.Slot

        # importing went okay, PySide must be available for use
        QT_AVAILABLE = True
        USING_PYSIDE2 = True

    # import failed. No Qt / UI bindings available...
    except ImportError:
        pass

print(f"[Tenet] USING_PYSIDE2={USING_PYSIDE2}")
