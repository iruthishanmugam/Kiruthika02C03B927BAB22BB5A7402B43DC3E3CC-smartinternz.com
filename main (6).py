class batsman:
  def __init__(self):
    self.strikerate=0.0
    self.totalruns=0
    self.highestscore=0
    self.battingrate=0
  def getbat(self,a,b,c,d):
    self.strikerate=a
    self.totalruns=b
    self.highestscore=c
    self.battingrate=d
  def dispbat(self):
    print("THE BATTING MAN")
    print("Strikerate:",self.strikerate)
    print("Totalruns",self.totalruns)
    print("Highestscore",self.highestscore)
    print("Battingrates",self.battingrate)
class bowler:
  def __init__(self):
    self.wickets=0
    self.economy=0.0
    self.hattricks=0
    self.bowlingrank=0
  def getbowl(self,e,f,g,h):
    self.wickets=e
    self.economy=f
    self.hattricks=g
    self.bowlingrank=h
  def dispbowl(self):
    print("THE BOWLER ")
    print("The wickets:",self.wickets)
    print("Economy:",self.economy)
    print("Hattricks:",self.hattricks)
    print("Bowlingrank:",self.bowlingrank)
class allrounder(batsman,bowler):
  def __init__(self):
    batsman.__init__(self)
    bowler.__init__(self)
    self.allrounderrank=0
  def getall(self,a,b,c,d,e,f,g,h,i):
    batsman.getbat(self,a,b,c,d)
    bowler.getbowl(self,e,f,g,h)
    self.allrounderrank=i
  def dispall(self):
    print("ALL ROUNDER ")
    print("All rounderrank:",self.allrounderrank)
    self.dispbat()
    self.dispbowl()
Jadeja=allrounder()
Jadeja.getall(145.51,2677,62,87,74,7.60,3,39,47)
Jadeja.dispall()