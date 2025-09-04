def decorStrFuction(func):
      def inner(n):
         result = func(n)
         result += " How are you ?"
         return result
      return inner

@decorStrFuction
def hello(name):
    return f"Hello {name}!! "

print(hello("Harsh"))
