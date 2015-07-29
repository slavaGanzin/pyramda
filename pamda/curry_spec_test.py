from functools import partial, wraps
from .curry_spec import *
from .private.asserts import \
    assert_equal, \
    assert_not_in_domain


def assert_isinstance(type, v):
    assert isinstance(v, type)


def curry_spec_creation_test():
    assert_isinstance(CurrySpec, CurrySpec(['x', 'y', 'z'], {'y': 5}))


def num_args_test():
    two_posn_three_kwarg_arg_values = ArgValues(
        [1, 2],
        {'foo': 5, 'bar': 7, 'baz': 10}
    )
    assert_equal(num_args(two_posn_three_kwarg_arg_values), 5)


def args_overlap_test():
    assert args_overlap(ArgValues([], {'foo': 1}), ArgValues([], {'foo': 10}))


def f(x, y, z=3):
    return x + y + z


def make_func_curry_spec_test():
    f_spec = make_func_curry_spec(f)
    assert_equal(f_spec, CurrySpec(['x', 'y', 'z'], {'z': 3}))


def remove_args_from_curry_spec_test():
    f_spec = make_func_curry_spec(f)
    arg_values = ArgValues([1], {'z': 10})
    removed_spec = remove_args_from_curry_spec(f_spec, arg_values)
    assert_equal(removed_spec, CurrySpec(['y', 'z'], {'z': 10}))
