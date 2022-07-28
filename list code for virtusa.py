list1=[1,2,3,4,5,6]#creating a list
ref_value=list1[0]#having a reference value to compare with the value in list1
flag=False#this flag is used to exit from the loops
for a in range(0,len(list1)):#creating a for loop to give index value for accessing the elements in the list1 
#the variabe index_value stores the element of the list1 using the index value 
  index_value=list1[a]
  if(a<=len(list1)-1):#this if loop is used for exiting the loop if the list ends

    print("reference value",ref_value)#this is a debugging statement remove if not needed
    print("index value",index_value)#this is a debugging  statement remove if not needed
    if(ref_value==index_value):#this if loop compares the refernce value with the element inside the list1
      ref_value=ref_value+1#if the code enters the loop the value of the reference value gets incemented by 1
    else: 
      flag=True#the value of flag changes from false to true 
      break#the block breaks out here
    if flag==True:#since the value of flag is true the code heres this if block
      break#this break is for the if block
  if flag==True:
    break   #this break is for the whie loop
if(a==len(list1)-1):#if all the value are equal the value of the a will be equAL TO THE length of the list hence 
  print("1")#the if block will print 1
else:#or if the value of a is not equal to length of the list1
  print("0")#if prints 0

#---------END OF CODE------------
		





