# Name: Ifemene Paul Chukwu
# Email: ifemenep@gmail.com
# Registration Number: M24B13/034
# Access No: B28325
# Course: BSc Information Technology
# Year: 2nd Year

class Profile:
    def __init__(self, name, favorite_language, hobby, tech_stack, github_username, fun_fact):
        self.name = name
        self.favorite_language = favorite_language
        self.hobby = hobby
        self.tech_stack = tech_stack
        self.github_username = github_username
        self.fun_fact = fun_fact

    def introduce(self):
        print(f"Hi, I’m {self.name}. I love {self.favorite_language} and my hobby is {self.hobby}.")
        print(f"Fun fact about me: {self.fun_fact}")

    def show_stack(self):
        print(f"{self.name}'s Tech Stack:")
        for tool in self.tech_stack:
            print(f" - {tool}")

    def github_link(self):
        return f"https://github.com/{self.github_username}"


if __name__ == "__main__":
    # Create your profile instance
    my_profile = Profile(
        name="Paul",
        favorite_language="Python",
        hobby="Chess",
        tech_stack=["Python", "Flask", "JavaScript", "Git", "HTML", "TailwindCSS"],
        github_username="ifemenepaul",
        fun_fact="I can debug code faster with music playing."
    )

    # Call the methods
    my_profile.introduce()
    my_profile.show_stack()
    print("GitHub Profile:", my_profile.github_link())