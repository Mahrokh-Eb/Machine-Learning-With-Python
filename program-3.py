'''
Programmer: Mahrokh Ebrahimi
Description: mobile phone app allows a user to press a button that starts a timer that counts seconds. 
When the user presses the button again, the timer stops. Draw a flowchart and write pseudocode that accepts 
the elapsed time in seconds and displays the value in minutes and remaining seconds. For example, 
if the elapsed time was 130 seconds, the output would be 2 minutes and 10 seconds.
Date: 6/22/2020 
'''

startPressButton = input('press a button that starts a timer that counts seconds!')
elapsedTime = int (input('elapsed time seconds?'))
mintues =round(elapsedTime / 60) 
seconds = elapsedTime % 60

endPressButton = input('press a button that ends a timer that counts seconds!')
print('mintues=', mintues, '   seconds=', seconds)


