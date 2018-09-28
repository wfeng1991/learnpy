from random import Random

def random_country():
    country=["country_a","country_b","country_c","country_d","country_f"]
    country_hotdegree = [1,10,7,5,9]

    c_range=[0]*len(country)
    for i,d in enumerate(country_hotdegree):
        c_range[i]=c_range[i-1]+d

    r = Random().randint(0,c_range[-1]-1)

    l,h=0,len(c_range)-1
    while l<=h:
        mid = (h+l)>>1
        if r>=c_range[mid]:
            l=mid+1
        else:
            h=mid-1
    return country[l]

    # i=0
    # while i<len(c_range):
    #     if i==0 and r<c_range[i]:
    #         return country[i]
    #     elif c_range[i-1]<=r<c_range[i]:
    #         return country[i]
    #     i+=1

print(random_country())
print(random_country())
print(random_country())
print(random_country())
print(random_country())