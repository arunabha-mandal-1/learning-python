# Command line argument processing using argparse in Python
import argparse
if __name__=="__main__":
    parser=argparse.ArgumentParser()
    # there are two types of arguments that argparse supports
        # 1. positional(number1, number2, operation)
        # 2. optional(-h, --help, --number1, --number2)
            # to make argument optional just add -- in front of argument name
        # python program_name.py -h
    
    # here we are writing a program that takes 3 inputs,
        # 1. first number
        # 2. second number
        # 3. operation("add", "subtract", "multiply")
        # it should return result of operation based on inputs
    
    # positional
    # parser.add_argument("number1", help="first number")
    # parser.add_argument("number2", help="second number")
    # parser.add_argument("operation", help="operation")
    # pyhton file_name.py num1 num2 op

    # optional
    # parser.add_argument("--number1", help="first number")
    # parser.add_argument("--number2", help="second number")
    # parser.add_argument("--operation", help="operation")
    # pyhton file_name.py --number1 num1 --number2 num2 --operation add
    # pyhton file_name.py --number1 num1 --operation add --number2 num2 

    # restrict user as soon as he inputs wrong input, program terminates
    parser.add_argument("--number1", help="first number")
    parser.add_argument("--number2", help="second number")
    parser.add_argument("--operation", help="operation", \
        choices=["add", "subtract", "multiply"])

    args=parser.parse_args()
    # print(args.number1)
    # print(args.number2)
    # print(args.operation)

    # when we pass anything to command line, it converted into an integer
    if args.number1: # checking if it does exist
        n1=int(args.number1)
    if args.number2: # checking if it does exist
        n2=int(args.number2)
    result=None
    if args.operation=='add':
        result=n1+n2
    elif args.operation=='subtract':
        result=n1-n2
    elif args.operation=='multiply':
        result=n1*n2
    else:
        print("unsupported operation")
    
    print("result is", result)