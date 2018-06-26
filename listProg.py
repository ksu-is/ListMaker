# list maker
print("CREATE A LIST".center(15,'='))
lis=[]
import shelve,os
if not os.path.exists('\\list):
    os.makedirs('\\list')

os.chdir('\\list')    
if 'listData.bat' in os.listdir('.'):
    shelf=shelve.open('listData')
    count=shelf['count']
else:
    shelf=shelve.open('listData')
    count=0
    shelf['count']=count
    shelf.close()
    shelf=shelve.open('listData')

print("Press Ctrl+C to exit the program")
while True:
    try:
        print("To create a list, enter 1")
        print("To view a list, enter 2")
        inp=int(input())
        if inp==1:
            name=input("What should we name the list?").strip()
            list_file=open('{}.txt' .format(name),'w+')

            user_input=' '
            print("Enter 'stop' to stop adding")
            while True:
                user_input=input("Enter an item to add to the list: ")
                user_input=user_input.strip().strip('\'').title()

                if user_input=='Stop':
                    break
                else:
                    lis.append(user_input)

            print("Creating a .txt file for you...")
            for i in range(len(lis)):
                list_file.write("{} {}\n" .format(i+1,lis[i]))
                
            list_file.close()

            print("Done!\nOpen P:\\Python practice\workshop\list to view the file")
            os.system('{}.txt' .format(name))
            choice=int(input("Do you want to see the contents?\nPress 1 for Yes. 0 for No "))
            if choice==1:
                for i in range(len(lis)):
                    print("{} {}" .format(i+1,lis[i]))
            elif choice==0:
                pass


        if inp==2:
            name=input("What is the name of the list? ")
            name=name+'.txt'
            if name in os.listdir('.'):
                list_file=open('{}' .format(name),'r+')
                for line in list_file:
                    print(line, end='')
                list_file.close()

            else:
                print("Sorry! The file was not found! ")

    except KeyboardInterrupt:
        print("Exiting")
        import sys
        sys.exit()

        
