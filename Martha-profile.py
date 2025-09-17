class Profile:
    def __init__(self, name, favorite_language, hobby, tech_stack, github_username, fun_fact):
        self.name = name
        self.favorite_language = favorite_language
        self.hobby = hobby
        self.tech_stack = tech_stack
        self.github_username = github_username
        self.fun_fact = fun_fact
    
    def introduce(self):
        print(f"Hi, I'm {self.name}. I love {self.favorite_language} and my hobby is {self.hobby}.")
    
    def show_stack(self):
        print(f"\n*** {self.name}'s Tech Stack ***")
        print("=" * 30)
        for i, tech in enumerate(self.tech_stack, 1):
            print(f"{i:2d}. {tech}")
        print("=" * 30)
    
    def github_link(self):
        return f"https://github.com/{self.github_username}"
    
    def display_profile(self):
        print("\n" + "="*50)
        print(f"           DEVELOPER PROFILE CARD")
        print("="*50)
        print(f"Name:               {self.name}")
        print(f"Favorite Language:  {self.favorite_language}")
        print(f"Hobby:              {self.hobby}")
        print(f"GitHub:             {self.github_link()}")
        print(f"Fun Fact:           {self.fun_fact}")
        print(f"Tech Stack:         {', '.join(self.tech_stack)}")
        print("="*50)

def main():
    my_profile = Profile(
        name="Martha Praise Katusiime",
        favorite_language="Python",
        hobby="Art",
        tech_stack=["Python", "Django", "Git", "PostgreSQL", "Docker", "React"],
        github_username="marthaea",
        fun_fact="I have github tiles as many as ants!"
    )
    
    # Calling all the required methods
    print("=== Profile Assignment Demo ===\n")
    
    # 1. Introduction
    my_profile.introduce()
    
    # 2. Showing tech stack
    my_profile.show_stack()
    
    # 3. GitHub link
    print(f"\n*** GitHub Profile: {my_profile.github_link()}")
    
    # 4. Complete profile display
    my_profile.display_profile()
    
    print(f"\n*** Fun Fact: {my_profile.fun_fact}")


# Template for creating my own profile
def create_your_profile():
    your_profile = Profile(
        name="Martha Praise Katusiime",  
        favorite_language="Python",  
        hobby="Art",  
        tech_stack=[  
            "React",
            "Python", 
            "Vue",
            "Django"
        ],
        github_username="marthaea",  
        fun_fact="Iam relentless"  # A fun fact about yourself
    )
    
    return your_profile


if __name__ == "__main__":
    main()
    
    
