class MultipleFunctions():
    #Subfields in AI
    def Subfields():
        list=['Machine Learning','Neural Networks','Vision','Robotics','Speech Processing','Natural Language Processing']
        print('Sub-fields in AI are:')
        for i in list:
            print(i)
    #To find Odd or EVEN
    def OddEven():
        value=float(input('enter a number:'))
        if(value%2==0):
            message=print(value,'is Even number')
        else:
            message=print(value,'is Odd number')
        return message
    #Marriage Eligibility
    def MarriageEligibility():
        Gender=(input('Your Gender:'))
        Age=int(input('Your Age:'))
        if(Gender=='male' and Age >=21):
            print('Eligible')
            law = 'Eligible'
        elif(Gender=='female' and Age>=18):
            print('Eligible')
            law= 'Eligible'
        else:
            print('Not Eligible')
            law='Not Eligible'
        return law
    
    #To find Percentage of the subjects
    def Percentage():
            subject=int(input('Subject1=')),int(input('Subject2=')),int(input('Subject3=')),int(input('Subject4=')),int(input('Subject5='))
            total=sum(subject)
            print('Total=',total)
            percent=float(total/5)
            print('Percentage=',percent)
            return percent
    #To find Area and Perimeter
    def triangle():
        height=float(input('Height='))
        breadth=float(input('Breadth='))
        print('Area formula: (height*breadth)/2')
        Area=(height*breadth)/2
        print ('Area of triangle:',Area)
        height1=float(input('Height1='))
        height2=float(input('Height2='))
        breadth=float(input('Breadth='))
        print('Perimeter formula: height1+height2+breadth')
        Perimeter=height1+height2+breadth
        print('Perimeter of triangle:',Perimeter)
        return Area, Perimeter