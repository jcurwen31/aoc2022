File file = new File("puzzle_day6_1")
def line, noOfLines = 0;
def list = new ArrayList<Integer>()
def result = 0
def myScore = 0
def winScore = 0

def start = 0
def end = 4
def currentMarker = ""
def ok = false
file.withReader { reader ->
        line = reader.readLine()
        while (!ok) {
            currentMarker = line.substring(start,end)
            println("currentMarker = $currentMarker")
            def chars = currentMarker.toCharArray().toSet()
            if (chars.size() != 4) {
                start++
                end++
            } else {
                ok = true
            }
        }
        println("currentMarker = $currentMarker and end = $end")
    }

