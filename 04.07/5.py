data = [
	{
		'name': "Cameron",
		'phone': "056-831-3152",
		'city': "Cotabato 'city'"
	},
	{
		'name': "Seth",
		'phone': "044-553-2450",
		'city': "Zwolle"
	},
	{
		'name': "Vivian",
		'phone': "099-562-4830",
		'city': "Körfez"
	},
	{
		'name': "Norman",
		'phone': "031-729-5627",
		'city': "Cajamarca"
	},
	{
		'name': "Drew",
		'phone': "088-307-3743",
		'city': "Ulloa (Barrial]"
	},
	{
		'name': "Ori",
		'phone': "003-003-3007",
		'city': "Gyeongju"
	},
	{
		'name': "Macy",
		'phone': "056-828-7277",
		'city': "Potchefstroom"
	},
	{
		'name': "Steven",
		'phone': "003-285-8078",
		'city': "Chía"
	},
	{
		'name': "Otto",
		'phone': "022-781-1413",
		'city': "Berlin"
	},
	{
		'name': "Silas",
		'phone': "073-863-3359",
		'city': "Béthune"
	},
	{
		'name': "Micah",
		'phone': "047-461-1967",
		'city': "Oldenzaal"
	},
	{
		'name': "Fay",
		'phone': "070-435-7758",
		'city': "Lorient"
	},
	{
		'name': "Olga",
		'phone': "023-195-4171",
		'city': "Burlington"
	},
	{
		'name': "Plato",
		'phone': "059-737-4733",
		'city': "Voronezh"
	},
	{
		'name': "Lucian",
		'phone': "040-465-3992",
		'city': "Christchurch"
	},
	{
		'name': "Scarlett",
		'phone': "096-284-6461",
		'city': "Saintes"
	},
	{
		'name': "Preston",
		'phone': "013-335-4256",
		'city': "Gwangyang"
	},
	{
		'name': "Jared",
		'phone': "081-432-2548",
		'city': "Winnipeg"
	},
	{
		'name': "Ali",
		'phone': "061-450-1232",
		'city': "Åkersberga"
	},
	{
		'name': "Brady",
		'phone': "026-438-5398",
		'city': "Galway"
	}
]

res = {}    
   
for k,v in [(key,d[key]) for d in data for key in d]:
    if k not in res: 
        res[k]=[v]
    else: 
        res[k].append(v)
        

