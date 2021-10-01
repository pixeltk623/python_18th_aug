# x = [10,5,15,7,6,18,3]
# w = [2,3,5,7,1,4,1]
# weight = 15

# for i = 1 to n 
#    do x[i] = 0 
# weight = 0 
# for i = 1 to n 
#    if weight + w[i] ≤ W #then  
#       x[i] = 1 
#       weight = weight + w[i] 
#    else 
#       x[i] = (W - weight) / w[i] 
#       weight = W 
#       break 
# return x



# print("check for prime")
# count=0
# userInput=int(input("enter the number"))
# if userInput<1:
# 	print("invalid number")
# else:
# 	if userInput==1:
# 		print("1 is special number")
# 	else:
# 		for x in range(1,userInput+1):
# 			# print(x)
# 			if userInput%x==0:
# 				count=count+1
# 		if count==2:
# 			print(userInput,"number is prime")
# 		else:
# 			print(userInput,"number is not prime")



# print("prime between 1-100")
# for x in range(1,101):
# 	count=0
# 	for y in range(1,x+1):
# 		if x%y==0:
# 			count=count+1
# 	if count==2:
# 		print(x,"prime")
# 	else:
# 		print(x,"not prime")





# p = [10,5,15,7,6,18,3]
# w = [2,3,5,7,1,4,1]
# W = 15
 
 
# bw=[]
# for i in range (len(p)):
#   t = int(p[i])/int(w[i])
#   bw.append(t)
# pr = []
# nw = []
# print(bw)

# key=lambda k: bw[k]

# print(sorted(range(len(bw)), key()))

# key = []
# for l in range(len(bw)):
# 	key=lambda k: bw[l]
# 	key.append(key)

# print(bw)
# exit()

# pr = sorted(range(len(bw)), key=lambda k: bw[k])

# #pr = bw.sort(reverse=True)


# print(pr)

# exit()
# pr.reverse()

# print(pr)

# profit = 0.0
# print(pr)
# for i in pr:
#   if (W>0 and w[i]<=W):
#     W=W-w[i]
#     profit +=p[i]
#     #print(profit)
#   elif W>0:
#     profit  = profit + W*(bw[i])
#     #W=W-w[i]
#   else:
#     break
# print(profit)


# Iterative method
# import time
# def inver(s):
#   p = []
#   t = []
#   for i in range(len(s)):
#     for j in range(i+1,len(s)):
#       if s[i]>s[j]:
#         t = [s[i],s[j]]
#           #t[1] = s[j]
#         p.append(t)
#   return p

# s=[8,9,1,2,4,6]


# print(inver(s))
			
		



def fact_rec(n):
  if n==0:
    return 1
  return n*fact_rec(n-1)
fact_rec(5)
print(fact_rec(5))    