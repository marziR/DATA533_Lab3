def bmicat(BMI):
   
    if BMI < 18.5:
        return 'UNDERWEIGHT'
        
    elif (BMI >= 18.5 and BMI <= 24.9):
        return 'HEALTHY'
        
    elif (BMI >= 25 and BMI <30):
        return 'OVERWEIGHT'
        
    elif (BMI >= 30 and BMI <= 35):
        return 'OBESE'
        
    else:
        return 'MORBIDLY OBESE'
		