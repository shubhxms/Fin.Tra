import pandas as pd
import matplotlib.pyplot as plt

inc = pd.read_csv('df.csv', index_col=0)
exp = pd.read_csv('outgo.csv', index_col=0)

while True:
    mnt = ['Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec','Jan','Feb','Mar']
    cmd = input('Fintra λ ')
    cmdl = cmd.split()

    if cmdl[0] == 'income':
        if cmdl[5] == '=':
            inc.loc[cmdl[2],cmdl[4]] = int(cmdl[6])
            print(inc)
        elif cmdl[5] == '+':    
            inc.loc[cmdl[2],cmdl[4]] += int(cmdl[6])
            print(inc)
    
    elif cmdl[0] == 'expense':
        if cmdl[5] == '=':
            exp.loc[cmdl[2],cmdl[4]] = int(cmdl[6])
            print(exp)
        elif cmdl[5] == '+':    
            exp.loc[cmdl[2],cmdl[4]] += int(cmdl[6])
            print(exp)

    elif cmd == 'show':
        print('Income Table:\n',inc)
        print('Expense Table:\n',exp)

    elif cmd == 'inbar':
        incs = input('Name any one income which you wanna observe in this bar chart: ')
        plt.bar(mnt, list(inc[incs]), label = incs, width = 0.5)
        plt.xlabel('Months')
        plt.ylabel('Income Categories')
        plt.legend()
        plt.show()

    elif cmd == 'exbar':
        exps = input('Name any one expense which you wanna observe in this bar chart: ')
        plt.bar(mnt, list(exp[exps]), label = exps, width = 0.5)
        plt.xlabel('Months')
        plt.ylabel('Expense Categories')
        plt.legend()
        plt.show() 
        
    elif cmd == 'exit':
        print('Saving and exiting... \nDone')
        inc.to_csv('df.csv')
        exp.to_csv('outgo.csv')
        break       
    else:
        print("Invalid Input, please try again")