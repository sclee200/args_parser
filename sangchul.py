
import argparse

def arithmetic_operation(a, b, c):
    
    res = None
    if c == "+":
        res = a + b
    elif c== "-":
        res = a -b
    elif c== "*":
        res = a *b
    elif c== "/":        
            res=a/b        
    elif c== "**":
        res = a **b
    elif c== "%":       
            res=a%b      
    elif c== "//":         
            res=a//b       
    if res != None:
        return res
 

if __name__ == '__main__':
   try:
        args = argparse.ArgumentParser()
        args.add_argument('-x','--xval', required=True, help="사칙연산 파리미터1")
        args.add_argument('-y','--yval', required=True, help="사칙연산 파리미터2")
        args.add_argument('-z','--zval', required=True, help="사칙연산 종류")
        argvar = vars(args.parse_args())
        a= argvar["xval"] 
        b= argvar["yval"] 
        c= argvar["zval"]
        result = arithmetic_operation(int(a), int(b), str(c).strip())
        print("연산 결과 : ", result)
   except Exception as e:
        print("오류 : ", e )
      
