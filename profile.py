##Create class for Profile
class Profile:
    def __init__(self, name, favourite_language, hobby, tech_stack, github_username, fun_fact):
        self.name=name
        self.favourite_language=favourite_language
        self.hobby=hobby
        self.tech_stack=tech_stack
        self.github_username=github_username
        self.fun_fact=fun_fact
       #self = current instance of class. Helps each object to store its own data
    
    ##Methods
    #Intro message
    def introduce(self):
        print(f"Hi, I'm {self.name}. I love {self.favourite_language} and my hobby is {self.hobby}")    
    
    #Showing tech stack
    def show_stack(self):
        print("My tech stack includes:")
        for tool in self.tech_stack:
            print(f"-{tool}")  
    
    #Github profile
    def github_link(self):
        return (f"https://github.com/{self.github_username}") # So it does not print "None"     

#Script to create and use profile
if __name__ == "__main__":#This line makes sure this code runs only when 'profile.py' is executed not when it's a module
    #Profile creation  
    my_profile=Profile(
        name="Magezi Richard Elijah (M24B13/019)",
        favourite_language="Python",
        hobby="Auto Mechanical Projects",
        tech_stack=["Python", "Django", "React","C++"],
        github_username="Plastimytes",
        fun_fact="I can run 100 metres in 10.95 seconds"
    )  

#Calling the methods
my_profile.introduce()
my_profile.show_stack()
print(f"Github Profile: {my_profile.github_link()}")

print(f"Fun Fact: {my_profile.fun_fact}")
