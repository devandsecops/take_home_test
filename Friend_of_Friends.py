"""
With the popularity of social networks these days, we often want to check if 
someone knows someone who knows someone else.  Here we see a simple graph with 
Alice having 3 friends Christine, Elise, and Zardoz.  Henry has 3 friends also, 
Bob, Dan, and Zardoz, but is not direct friends with Alice.  Henry is however a 
Friend of a Friend.of Alice. Friendship is a two-way street.  
If A is a friend of B, then B is a friend of A.
"""

class Person(object):

  def __init__(self, unique_id, name, friends=None):
    self.unique_id = unique_id
    self.name = name
    if friends:
      self.friends = friends
    else:
      self.friends = {}
        
  def GetFriends(self):
    return self.friends
        
  def GetID(self):
    return self.unique_id
   
  def GetName(self):
    return self.name

  def AddFriend(self, person):
    self.friends[person.GetID()] = person    
    
  def IsFriend(self, person):
    return person.GetID() in self.friends      
        
def FriendOfFriend(user_a, user_b):
  friends_of_a = user_a.GetFriends()
  for friend in friends_of_a.values():
    print(friend.GetID())
    if friend.IsFriend(user_b):
      return True    
  return False      
          
p1 = Person(1, "Alice")
p2 = Person(2, "Bob")
p3 = Person(3, "Christine")
p4 = Person(4, "Dan")
p5 = Person(5, "Elise")
p6 = Person(6, "Frank")
p7 = Person(7, "Gertrude")
p8 = Person(8, "Henry")
p9 = Person(9, "Isabelle")
p10 = Person(10, "Zardoz")

p1.AddFriend(p2)
p1.AddFriend(p3)
p1.AddFriend(p4)

p4.AddFriend(p1)
p4.AddFriend(p5)

p5.AddFriend(p4)
p5.AddFriend(p6)
p5.AddFriend(p7)

p6.AddFriend(p8)
p6.AddFriend(p9)
p6.AddFriend(p10)

print(FriendOfFriend(p1,p5))
print(FriendOfFriend(p5, p6))