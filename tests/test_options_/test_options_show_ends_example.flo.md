[37m#example mission box1.flo[39;49;00m[37m[39;49;00m$
[37m#from: https://github.com/ioflo/ioflo[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[34mhouse[39;49;00m[37m [39;49;00mbox1[37m[39;49;00m$
[37m[39;49;00m$
[37m   [39;49;00m[34mframer[39;49;00m[37m [39;49;00mvehiclesim[37m [39;49;00m[35mbe[39;49;00m[37m [39;49;00mactive[37m [39;49;00m[36mfirst[39;49;00m[37m [39;49;00mvehicle_run[37m[39;49;00m$
[37m      [39;49;00m[34mframe[39;49;00m[37m [39;49;00mvehicle_run[37m[39;49;00m$
[37m         [39;49;00m[36mdo[39;49;00m[37m [39;49;00msimulator[37m [39;49;00mmotion[37m [39;49;00muuv[37m[39;49;00m$
[37m[39;49;00m$
[37m   [39;49;00m[34mframer[39;49;00m[37m [39;49;00mmission[37m [39;49;00m[35mbe[39;49;00m[37m [39;49;00mactive[37m [39;49;00m[36mfirst[39;49;00m[37m [39;49;00mnorthleg[37m[39;49;00m$
[37m      [39;49;00m[34mframe[39;49;00m[37m [39;49;00mnorthleg[37m[39;49;00m$
[37m         [39;49;00m[36mset[39;49;00m[37m [39;49;00melapsed[37m [39;49;00m[35mwith[39;49;00m[37m [39;49;00m[34m20.0[39;49;00m[37m[39;49;00m$
[37m         [39;49;00m[36mset[39;49;00m[37m [39;49;00mheading[37m [39;49;00m[35mwith[39;49;00m[37m [39;49;00m[34m0.0[39;49;00m[37m[39;49;00m$
[37m         [39;49;00m[36mset[39;49;00m[37m [39;49;00mdepth[37m [39;49;00m[35mwith[39;49;00m[37m [39;49;00m[34m5.0[39;49;00m[37m[39;49;00m$
[37m         [39;49;00m[36mset[39;49;00m[37m [39;49;00mspeed[37m [39;49;00m[35mwith[39;49;00m[37m [39;49;00m[34m2.5[39;49;00m[37m[39;49;00m$
[37m         [39;49;00m[36mgo[39;49;00m[37m [39;49;00m[36mnext[39;49;00m[37m [39;49;00m[35mif[39;49;00m[37m [39;49;00melapsed[37m [39;49;00m>=[37m [39;49;00mgoal[37m[39;49;00m$
[37m[39;49;00m$
[37m      [39;49;00m[34mframe[39;49;00m[37m [39;49;00meastleg[37m[39;49;00m$
[37m         [39;49;00m[36mset[39;49;00m[37m [39;49;00mheading[37m [39;49;00m[35mwith[39;49;00m[37m [39;49;00m[34m90.0[39;49;00m[37m[39;49;00m$
[37m         [39;49;00m[36mgo[39;49;00m[37m [39;49;00m[36mnext[39;49;00m[37m [39;49;00m[35mif[39;49;00m[37m [39;49;00melapsed[37m [39;49;00m>=[37m [39;49;00mgoal[37m[39;49;00m$
[37m[39;49;00m$
[37m      [39;49;00m[34mframe[39;49;00m[37m [39;49;00msouthleg[37m[39;49;00m$
[37m         [39;49;00m[36mset[39;49;00m[37m [39;49;00mheading[37m [39;49;00m[35mwith[39;49;00m[37m [39;49;00m[34m180.0[39;49;00m[37m[39;49;00m$
[37m         [39;49;00m[36mgo[39;49;00m[37m [39;49;00m[36mnext[39;49;00m[37m [39;49;00m[35mif[39;49;00m[37m [39;49;00melapsed[37m [39;49;00m>=[37m [39;49;00mgoal[37m[39;49;00m$
[37m[39;49;00m$
[37m      [39;49;00m[34mframe[39;49;00m[37m [39;49;00mwestleg[37m[39;49;00m$
[37m         [39;49;00m[36mset[39;49;00m[37m [39;49;00mheading[37m [39;49;00m[35mwith[39;49;00m[37m [39;49;00m[34m270.0[39;49;00m[37m[39;49;00m$
[37m         [39;49;00m[36mgo[39;49;00m[37m [39;49;00m[36mnext[39;49;00m[37m [39;49;00m[35mif[39;49;00m[37m [39;49;00melapsed[37m [39;49;00m>=[37m [39;49;00mgoal[37m[39;49;00m$
[37m[39;49;00m$
[37m      [39;49;00m[34mframe[39;49;00m[37m [39;49;00mmission_stop[37m[39;49;00m$
[37m         [39;49;00m[36mbid[39;49;00m[37m [39;49;00m[36mstop[39;49;00m[37m [39;49;00mvehiclesim[37m[39;49;00m$
[37m         [39;49;00m[36mbid[39;49;00m[37m [39;49;00m[36mstop[39;49;00m[37m [39;49;00mautopilot[37m[39;49;00m$
[37m         [39;49;00m[36mbid[39;49;00m[37m [39;49;00m[36mstop[39;49;00m[37m [39;49;00mme[37m[39;49;00m$
[37m[39;49;00m$
[37m   [39;49;00m[34mframer[39;49;00m[37m [39;49;00mautopilot[37m [39;49;00m[35mbe[39;49;00m[37m [39;49;00mactive[37m [39;49;00m[36mfirst[39;49;00m[37m [39;49;00mautopilot_run[37m[39;49;00m$
[37m      [39;49;00m[34mframe[39;49;00m[37m [39;49;00mautopilot_run[37m[39;49;00m$
[37m         [39;49;00m[36mdo[39;49;00m[37m [39;49;00mcontroller[37m [39;49;00mpid[37m [39;49;00mspeed[37m[39;49;00m$
[37m         [39;49;00m[36mdo[39;49;00m[37m [39;49;00mcontroller[37m [39;49;00mpid[37m [39;49;00mheading[37m[39;49;00m$
[37m         [39;49;00m[36mdo[39;49;00m[37m [39;49;00mcontroller[37m [39;49;00mpid[37m [39;49;00mdepth[37m[39;49;00m$
[37m         [39;49;00m[36mdo[39;49;00m[37m [39;49;00mcontroller[37m [39;49;00mpid[37m [39;49;00mpitch$
