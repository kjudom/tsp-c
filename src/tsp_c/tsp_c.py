# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_tsp_c')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_tsp_c')
    _tsp_c = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_tsp_c', [dirname(__file__)])
        except ImportError:
            import _tsp_c
            return _tsp_c
        try:
            _mod = imp.load_module('_tsp_c', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _tsp_c = swig_import_helper()
    del swig_import_helper
else:
    import _tsp_c
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0

class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _tsp_c.delete_SwigPyIterator
    __del__ = lambda self: None

    def value(self):
        return _tsp_c.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _tsp_c.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _tsp_c.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _tsp_c.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _tsp_c.SwigPyIterator_equal(self, x)

    def copy(self):
        return _tsp_c.SwigPyIterator_copy(self)

    def next(self):
        return _tsp_c.SwigPyIterator_next(self)

    def __next__(self):
        return _tsp_c.SwigPyIterator___next__(self)

    def previous(self):
        return _tsp_c.SwigPyIterator_previous(self)

    def advance(self, n):
        return _tsp_c.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _tsp_c.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _tsp_c.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _tsp_c.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _tsp_c.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _tsp_c.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _tsp_c.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self
SwigPyIterator_swigregister = _tsp_c.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

class VecDouble(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, VecDouble, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, VecDouble, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _tsp_c.VecDouble_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _tsp_c.VecDouble___nonzero__(self)

    def __bool__(self):
        return _tsp_c.VecDouble___bool__(self)

    def __len__(self):
        return _tsp_c.VecDouble___len__(self)

    def __getslice__(self, i, j):
        return _tsp_c.VecDouble___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _tsp_c.VecDouble___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _tsp_c.VecDouble___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _tsp_c.VecDouble___delitem__(self, *args)

    def __getitem__(self, *args):
        return _tsp_c.VecDouble___getitem__(self, *args)

    def __setitem__(self, *args):
        return _tsp_c.VecDouble___setitem__(self, *args)

    def pop(self):
        return _tsp_c.VecDouble_pop(self)

    def append(self, x):
        return _tsp_c.VecDouble_append(self, x)

    def empty(self):
        return _tsp_c.VecDouble_empty(self)

    def size(self):
        return _tsp_c.VecDouble_size(self)

    def swap(self, v):
        return _tsp_c.VecDouble_swap(self, v)

    def begin(self):
        return _tsp_c.VecDouble_begin(self)

    def end(self):
        return _tsp_c.VecDouble_end(self)

    def rbegin(self):
        return _tsp_c.VecDouble_rbegin(self)

    def rend(self):
        return _tsp_c.VecDouble_rend(self)

    def clear(self):
        return _tsp_c.VecDouble_clear(self)

    def get_allocator(self):
        return _tsp_c.VecDouble_get_allocator(self)

    def pop_back(self):
        return _tsp_c.VecDouble_pop_back(self)

    def erase(self, *args):
        return _tsp_c.VecDouble_erase(self, *args)

    def __init__(self, *args):
        this = _tsp_c.new_VecDouble(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def push_back(self, x):
        return _tsp_c.VecDouble_push_back(self, x)

    def front(self):
        return _tsp_c.VecDouble_front(self)

    def back(self):
        return _tsp_c.VecDouble_back(self)

    def assign(self, n, x):
        return _tsp_c.VecDouble_assign(self, n, x)

    def resize(self, *args):
        return _tsp_c.VecDouble_resize(self, *args)

    def insert(self, *args):
        return _tsp_c.VecDouble_insert(self, *args)

    def reserve(self, n):
        return _tsp_c.VecDouble_reserve(self, n)

    def capacity(self):
        return _tsp_c.VecDouble_capacity(self)
    __swig_destroy__ = _tsp_c.delete_VecDouble
    __del__ = lambda self: None
VecDouble_swigregister = _tsp_c.VecDouble_swigregister
VecDouble_swigregister(VecDouble)

class VecInt(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, VecInt, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, VecInt, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _tsp_c.VecInt_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _tsp_c.VecInt___nonzero__(self)

    def __bool__(self):
        return _tsp_c.VecInt___bool__(self)

    def __len__(self):
        return _tsp_c.VecInt___len__(self)

    def __getslice__(self, i, j):
        return _tsp_c.VecInt___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _tsp_c.VecInt___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _tsp_c.VecInt___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _tsp_c.VecInt___delitem__(self, *args)

    def __getitem__(self, *args):
        return _tsp_c.VecInt___getitem__(self, *args)

    def __setitem__(self, *args):
        return _tsp_c.VecInt___setitem__(self, *args)

    def pop(self):
        return _tsp_c.VecInt_pop(self)

    def append(self, x):
        return _tsp_c.VecInt_append(self, x)

    def empty(self):
        return _tsp_c.VecInt_empty(self)

    def size(self):
        return _tsp_c.VecInt_size(self)

    def swap(self, v):
        return _tsp_c.VecInt_swap(self, v)

    def begin(self):
        return _tsp_c.VecInt_begin(self)

    def end(self):
        return _tsp_c.VecInt_end(self)

    def rbegin(self):
        return _tsp_c.VecInt_rbegin(self)

    def rend(self):
        return _tsp_c.VecInt_rend(self)

    def clear(self):
        return _tsp_c.VecInt_clear(self)

    def get_allocator(self):
        return _tsp_c.VecInt_get_allocator(self)

    def pop_back(self):
        return _tsp_c.VecInt_pop_back(self)

    def erase(self, *args):
        return _tsp_c.VecInt_erase(self, *args)

    def __init__(self, *args):
        this = _tsp_c.new_VecInt(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def push_back(self, x):
        return _tsp_c.VecInt_push_back(self, x)

    def front(self):
        return _tsp_c.VecInt_front(self)

    def back(self):
        return _tsp_c.VecInt_back(self)

    def assign(self, n, x):
        return _tsp_c.VecInt_assign(self, n, x)

    def resize(self, *args):
        return _tsp_c.VecInt_resize(self, *args)

    def insert(self, *args):
        return _tsp_c.VecInt_insert(self, *args)

    def reserve(self, n):
        return _tsp_c.VecInt_reserve(self, n)

    def capacity(self):
        return _tsp_c.VecInt_capacity(self)
    __swig_destroy__ = _tsp_c.delete_VecInt
    __del__ = lambda self: None
VecInt_swigregister = _tsp_c.VecInt_swigregister
VecInt_swigregister(VecInt)

class VecVecdouble(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, VecVecdouble, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, VecVecdouble, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _tsp_c.VecVecdouble_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _tsp_c.VecVecdouble___nonzero__(self)

    def __bool__(self):
        return _tsp_c.VecVecdouble___bool__(self)

    def __len__(self):
        return _tsp_c.VecVecdouble___len__(self)

    def __getslice__(self, i, j):
        return _tsp_c.VecVecdouble___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _tsp_c.VecVecdouble___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _tsp_c.VecVecdouble___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _tsp_c.VecVecdouble___delitem__(self, *args)

    def __getitem__(self, *args):
        return _tsp_c.VecVecdouble___getitem__(self, *args)

    def __setitem__(self, *args):
        return _tsp_c.VecVecdouble___setitem__(self, *args)

    def pop(self):
        return _tsp_c.VecVecdouble_pop(self)

    def append(self, x):
        return _tsp_c.VecVecdouble_append(self, x)

    def empty(self):
        return _tsp_c.VecVecdouble_empty(self)

    def size(self):
        return _tsp_c.VecVecdouble_size(self)

    def swap(self, v):
        return _tsp_c.VecVecdouble_swap(self, v)

    def begin(self):
        return _tsp_c.VecVecdouble_begin(self)

    def end(self):
        return _tsp_c.VecVecdouble_end(self)

    def rbegin(self):
        return _tsp_c.VecVecdouble_rbegin(self)

    def rend(self):
        return _tsp_c.VecVecdouble_rend(self)

    def clear(self):
        return _tsp_c.VecVecdouble_clear(self)

    def get_allocator(self):
        return _tsp_c.VecVecdouble_get_allocator(self)

    def pop_back(self):
        return _tsp_c.VecVecdouble_pop_back(self)

    def erase(self, *args):
        return _tsp_c.VecVecdouble_erase(self, *args)

    def __init__(self, *args):
        this = _tsp_c.new_VecVecdouble(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def push_back(self, x):
        return _tsp_c.VecVecdouble_push_back(self, x)

    def front(self):
        return _tsp_c.VecVecdouble_front(self)

    def back(self):
        return _tsp_c.VecVecdouble_back(self)

    def assign(self, n, x):
        return _tsp_c.VecVecdouble_assign(self, n, x)

    def resize(self, *args):
        return _tsp_c.VecVecdouble_resize(self, *args)

    def insert(self, *args):
        return _tsp_c.VecVecdouble_insert(self, *args)

    def reserve(self, n):
        return _tsp_c.VecVecdouble_reserve(self, n)

    def capacity(self):
        return _tsp_c.VecVecdouble_capacity(self)
    __swig_destroy__ = _tsp_c.delete_VecVecdouble
    __del__ = lambda self: None
VecVecdouble_swigregister = _tsp_c.VecVecdouble_swigregister
VecVecdouble_swigregister(VecVecdouble)

class PairVecDouble(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, PairVecDouble, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, PairVecDouble, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _tsp_c.new_PairVecDouble(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_setmethods__["first"] = _tsp_c.PairVecDouble_first_set
    __swig_getmethods__["first"] = _tsp_c.PairVecDouble_first_get
    if _newclass:
        first = _swig_property(_tsp_c.PairVecDouble_first_get, _tsp_c.PairVecDouble_first_set)
    __swig_setmethods__["second"] = _tsp_c.PairVecDouble_second_set
    __swig_getmethods__["second"] = _tsp_c.PairVecDouble_second_get
    if _newclass:
        second = _swig_property(_tsp_c.PairVecDouble_second_get, _tsp_c.PairVecDouble_second_set)
    def __len__(self):
        return 2
    def __repr__(self):
        return str((self.first, self.second))
    def __getitem__(self, index): 
        if not (index % 2):
            return self.first
        else:
            return self.second
    def __setitem__(self, index, val):
        if not (index % 2):
            self.first = val
        else:
            self.second = val
    __swig_destroy__ = _tsp_c.delete_PairVecDouble
    __del__ = lambda self: None
PairVecDouble_swigregister = _tsp_c.PairVecDouble_swigregister
PairVecDouble_swigregister(PairVecDouble)


def solve_greedy(d_matrix):
    return _tsp_c.solve_greedy(d_matrix)
solve_greedy = _tsp_c.solve_greedy

def solve_SA(d_matrix):
    return _tsp_c.solve_SA(d_matrix)
solve_SA = _tsp_c.solve_SA

def set_param_SA(C0, Cmin, L0, alpha):
    return _tsp_c.set_param_SA(C0, Cmin, L0, alpha)
set_param_SA = _tsp_c.set_param_SA

def solve_PSO(d_matrix):
    return _tsp_c.solve_PSO(d_matrix)
solve_PSO = _tsp_c.solve_PSO

def set_param_ACO(hconst, alpha, beta, evprate, intsty, nAnt, nItr):
    return _tsp_c.set_param_ACO(hconst, alpha, beta, evprate, intsty, nAnt, nItr)
set_param_ACO = _tsp_c.set_param_ACO

def solve_ACO(d_matrix):
    return _tsp_c.solve_ACO(d_matrix)
solve_ACO = _tsp_c.solve_ACO
# This file is compatible with both classic and new-style classes.


