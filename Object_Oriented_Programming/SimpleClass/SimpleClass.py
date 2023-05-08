class Snake:
    name="Nitin"

    def modifyname(self, new_name):
        self.name=new_name

snake1=Snake()
print(snake1.name)
snake1.modifyname("Python")
print(snake1.name)