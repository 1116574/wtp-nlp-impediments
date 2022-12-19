# This is from old version, pls update.
*a slight update was done, but an overhaul is needed*
```
<class 'wtp_nlp.data.status.Double_Loop'>,
            [
                < Kabaty >,
                < Natolin >,
                < Imielin >,
                < Stokłosy >,
                < Ursynów >,
                < Służew >,
                # (NOTE: this should be split)
                < Marymont >,
                < Słodowiec >,
                < Stare Bielany >,
                < Wawrzyszew >,
                < Młociny >
            ]
```
for M1 and 
```
<class 'wtp_nlp.data.status.Double_Loop'>, [< Bemowo >, < Ulrychów >, (again, split here), < Szwedzka >, < Targówek Mieszkaniowy >, < Trocka >]
```
for M2
# Permitted output
## General status
Quick overview of possible states

### ok
The service is running normally.
### degraded
~~TODO: Degraded status is currently unaviable in normal output.~~ *i think it is now as `degraded_line` and `degraded_segment`?*
There are (possibly undefinied) delays on the network or between stations, or there are less trains than usual. (doc: tokens `Delays` and `Reduced_Service`)
### loop/double_loop
Service operates in a loop, like when last 3 stations are offline, or 2 distinct loops, e.g. when center section is offline then services are split into northern and southern loops. (doc: tokens `Shortened_Service`, `Not_Functioning_Service` and `Not_Functioning_Station`)
### facilities
Some facilities such as elevators or exits dont work. (doc: token `Not_Functioning_Facility`)

## Additional information
For `degraded` and `loop`/`double_loop` there might be information about replacement services (wheater they exist or not, doc: `Metro_Replacement_Names`, `Replaement_Service`), the reason for problems (technical, malfunction, a 'situation' docs: `Reason(...)`), or about other services whose normal routes are extended or otherwise changed to accomodate for disabled metro services (doc: token `Detour_By_Extension`).