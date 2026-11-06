class DailyTemperatures:
    # stack method:
    def dailyTemperatures(self,temps:list[int])->list[int]:
        res=[0]*len(temps)
        stack:list[int]=[]
        for i in range(len(temps)-1,-1,-1):
            cur =temps[i]
            while stack and cur> temps[stack[-1]]:
                stack.pop()
            if stack :
                res[i]=stack[-1]-i
            stack.append(i)

        return res


if __name__=="__main__":
    obj =DailyTemperatures()
    temperatures = [30,38,30,36,35,40,28]
    print(obj.dailyTemperatures(temperatures))
    temperatures = [22,21,20]
    print(obj.dailyTemperatures(temperatures))
