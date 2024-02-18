import time
import os
#These imports are needed to run this function corretly.

def loading_spin():
    
    def clearingline():
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console 

    loop = 0
    progress_loading = 0 # 0%
    elements = ['|', '/', '-', '\\', '|',  '|', '\\', '-', '/', '|']
    loaded_elements = [' ','\033[93m*=0%\033[0m']
    clearingline()
    while loop == 0:
        counter = 0
        for i in elements:
            if progress_loading >= 100:
                print('\n  \033[92mApplication Loading Complete\033[0m')
                loop = 1
                break
            else:   
                print(i, end='\r')
                time.sleep(0.2) # 0.2 seconds
                progress_loading += 1
                counter += 1
                if counter == 5:
                    clearingline()
                    if progress_loading < 30: 
                        loaded_elements.append('\033[91m*\033[0m')
                        loaded_elements[1] = str(progress_loading) + '%'
                        print('\n' + ' '.join(loaded_elements), end='\r')
                        counter = 0
                    elif progress_loading < 70:
                        loaded_elements.append('\033[93m*\033[0m')
                        loaded_elements[1] = str(progress_loading) + '%'
                        print('\n' + ' '.join(loaded_elements), end='\r')
                        counter = 0
                    else:
                        loaded_elements.append('\033[92m*\033[0m')
                        loaded_elements[1] = str(progress_loading) + '%'
                        print('\n' + ' '.join(loaded_elements), end='\r')
                        counter = 0
                


loading_spin() 
# For implementation, just call the function loading_spin() in your code.
# To add the animation to loading software this function will need to be called with an argument. 
# e.g. pass progress_loading as a number to the function to show the progress of the loading.