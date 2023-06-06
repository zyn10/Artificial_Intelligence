from kanren import Relation, facts,run,var
parent=Relation()
facts(parent, ("Umer", "Usman"), ("Umer", "Ali"),("Suleman", "Umer"))
dummy=var()
x=var()
y=var()

print("Father of Usman      : ",run(1,dummy,parent(dummy,"Usman")))
print("Children of Usman    : ",run(2,x, parent('Umer',y),parent('Umer',x)))
print("Grandfather of Usman : ",run(1, x, parent(x, y),parent(y, 'Usman')))