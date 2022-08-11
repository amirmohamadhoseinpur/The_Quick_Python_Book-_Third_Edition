'''QUICK CHECK: NAMESPACES AND SCOPE Consider a variable width that’s in
the module make_window.py. In which of the following contexts is width in
scope?:
(A) within the module itself
(B) inside the resize() function in the module
(C) within the script that imported the make_window.py module'''

# A ------->   width is in this scope.
# B ------->   width is in this scope.
# C ------->   width isn't in this scope but make_window.width refers to it.