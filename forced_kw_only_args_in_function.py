# https://peps.python.org/pep-3102/

# 1) * as first argument
# This function accepts any number of positional arguments, and it also accepts a keyword option called ‘case_sensitive’.
# This option will never be filled in by a positional argument, but must be explicitly specified by name.

def fun_a(*pos_args, kw_arg=True):
    print(f"fun_a: {pos_args}")
    return pos_args
print(type(fun_a(10,20,30))) # (10,20,30) - all positional args are now in tuple

def fun_b(*pos_args, kw_arg=True):
    print(f"fun_b_pos_args: {pos_args}")
    print(f"fun_b_kw_arg: {kw_arg}")
fun_b(10,20,30)  # (10,20,30) + True
fun_b(10,20,kw_arg=False)  # (10,20) + False
fun_b(kw_arg=10) # () + 10 -> if no pos_args -> empty tuple ()
# fun_b(kw_arg=False, 20, 30) SyntaxError: positional argument follows keyword argument
# fun_b(other_kw=10, kw_arg=20) TypeError: fun_b() got an unexpected keyword argument 'other_kw'
# fun_b(kw_arg=10, other_kw=20) TypeError: fun_b() got an unexpected keyword argument 'other_kw'

# 2) * in the midle of arguments
# Allow the argument name to be omitted for a varargs argument. The meaning of this is to allow for keyword-only arguments for
# functions that would not otherwise take a varargs argument

def fun_c(a,b,c=1,d=2,e=3): # in normal kw could be override by positional args
    print(f"fun_c: {a,b,c,d,e}")
fun_c(10,20) # 10 20 1 2 3
fun_c(10,20,30,40,50) # 10 20 30 40 50
# fun_c(10) TypeError: fun_c() missing 1 required positional argument: 'b'

def fun_d(a,b,*,c=1,d=2,e=3): # kwargs could not be override by positional args, only be kw
    print(f"fun_d: {a,b,c,d,e}")
fun_d(10,20) # 10 20 1 2 3
fun_d(10,20,c=30,d=40,e=50) # 10 20 30 40 50
#  fun_d(10,20,30,40,50) TypeError: fun_d() takes 2 positional arguments but 5 were given
