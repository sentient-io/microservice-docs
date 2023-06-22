
# def parent(func):
#   def inner(a,b):
#       if b==0:
#          return False
#       else:
#         return func(a,b)
#   return inner 

# @parent
# def decod(a,b):
#   dev= a/b
#   return  dev

# print(decod(10,0))

# def parent(func):
#     def child():
#         data=func()
#         result=data.upper()
#         return result
#     return child
        
# def main():
#     return "I am the main function "

# Result=parent(main)
# print(Result())

def grandfather(strg):
  def parent(func):
      def child(a,b):
          if b !=0:
              result=func(a,b)
              print(result)
              return str(result) +strg
          else:
              return "Can't divide by zero"+strg
      return child
  return parent
@grandfather(" i am a granfather ")        
def div(a,b):
    result=a/b
    return result

result=div(100,0)
print(result)


 