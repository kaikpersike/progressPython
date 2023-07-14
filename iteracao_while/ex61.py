#Sequencia IJ 4
i = 0.2
iI = 1.2
j = 2
jJ = 2
print(f"I={0} J=1")
print(f"I={0} J=2")
print(f"I={0} J=3")
while i<1:
    print(f"I={i:.1f} J=1.{j}")
    print(f"I={i:.1f} J=2.{j}")
    print(f"I={i:.1f} J=3.{j}")
    j+=2
    i+=0.2
print(f"I={1} J=2")
print(f"I={1} J=3")
print(f"I={1} J=4")
while iI <1.9:
    print(f"I={iI:.1f} J=2.{jJ}")
    print(f"I={iI:.1f} J=3.{jJ}")
    print(f"I={iI:.1f} J=4.{jJ}")
    jJ+=2
    iI+=0.2
print(f"I={2} J=3")
print(f"I={2} J=4")
print(f"I={2} J=5")