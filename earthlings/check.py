def moderate(marks, passMarks):
      if marks==passMarks-1 or marks==passMarks-2:
                 marks=passMarks
      return marks

def main(): # name can be anything but while calling in line 13 it should be the same
     passMarks=40
     marks=input('Enter marks: ')
     marksInInteger=int(marks)
     moderateMarks=moderate(marksInInteger, passMarks)
     print("Your moderated marks is:", moderateMarks)

if __name__=='__main__':
    main()