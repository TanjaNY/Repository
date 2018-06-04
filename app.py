# 1. Import Flask
from flask import Flask
app = Flask(__name__)
@app.route("/api/v1.0/precipitation")
def precipitation():
    year_ago=dt.date.today()-dt.timedelta(365)
    presults = session.query(Measurement.date,Measurement.tobs).\
    filter(Measurement.date > year_ago).all()
    
    prec_all=[]
    
    for measurement in presults
        prec_dict={}
        prec_dict['date'].key()=Measurement.date
        prec_dict['tobs'].value()=Measurement.tobs
        prec_all.append(prec_dict)
    
return jsonsfy(prec_all=[]) 

@app.route("/api/v1.0/stations")
def stations():
    sresult=session.query(distinct(Measurement.station).all()
    stations_all=[] 
    for station in sresult
    stations_all.append(station) 
                          
return jsonsfy(stations_all) 
                        
                          
@app.route("/api/v1.0/tobs")
def tobs():
    tresults=session.query(Measurement.tobs).\
             filter(Measurement.date > year_ago)
     tobs_all=[]
    for tob in tresults
    tobs_all.append(tob)
                          
@app.route("/api/v1.0/<start>")
def calc01 ():
    qu=[Measurement.tobs,
                    func.avg(Measurement.tobs),
                    func.max(Measurement.tobs),
                    func.min(Measurement.tobs)
                     ]
    cresult=session.query(*qu).\
                filter(Measurement.date > star_date).al()
print("TVAG,TMAX and TMIN are:",cresult)
                          
@app.route("/api/v1.0/<start>/<end>")

calc_temps(start_date,end_date)                         
print("TVAG,TMAX and TMIN are:",res_list)    
                