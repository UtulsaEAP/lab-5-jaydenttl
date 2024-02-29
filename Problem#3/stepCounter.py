'''
Name: Jayden Ly
Lab Time: thurs 11:35 AM
'''
def feet_to_steps(user_feet):
   return (user_feet / 2.5)

if __name__ == '__main__':
    user_feet = float(input())
    steps_taken = feet_to_steps(user_feet)
    print(int(steps_taken))