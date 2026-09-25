import json, os

def writing():
#	global totalseconds, sessions
	if basevars.totalseconds <= 0: return
	today = datetime.now().strftime("%d/%m/%y")

	base = os.path.dirname(os.path.abspath(__file__))
	datdir = os.path.join(base, "data")
	os.makedirs(datdir, exist_ok = True)
	file = os.path.join(datdir, "statistics.json")
	data = {}

	if os.path.exists(file):
		try:
			with open(file, "r") as f:
				data = json.load(f)
		except (json.JSONDecodeError, ValueError):
			print("⚠️ битий JSON, створюю новий файл")
			data = {}
			
	entry = {
        "sessions": sessions,
        "time": f"{basevars.totalseconds//3600}h {(basevars.totalseconds%3600)//60}m {basevars.totalseconds%60}s",
        "time_seconds": basevars.totalseconds
        }

	if today not in data:
		data[today] = []
	data[today].append(entry)
	
	tmp_file = file + ".tmp"
    
	with open(tmp_file, "w") as f: 
		json.dump(data, f, indent=4)
		f.flush()
		os.fsync(f.fileno())
	os.replace(tmp_file, file)

if __name__ == "__main__":
    print("\033[?25l")
    t = threading.Thread(target=inputs, daemon=True)
    t.start()
    try: main()
    finally:
        writing()
        showstats()
