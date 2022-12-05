
//def liste = ['Groovy', 'is', 'great!']
//
//// Remove last item from list
//// with pop().
//assert liste.pop() == 'great!'
//assert liste == ['Groovy', 'is']

File file = new File("puzzle_day5_1")
def line, noOfLines = 0;
def list = new ArrayList<Integer>()
def total = 0
def myScore = 0
def winScore = 0

def mapIndexes = [
        "1" : "1",
        "5" : "2",
        "9" : "3",
        "13": "4",
        "17": "5",
        "21": "6",
        "25": "7",
        "29": "8",
        "33": "9"
]

def columns = [
        "1": [],
        "2": [],
        "3": [],
        "4": [],
        "5": [],
        "6": [],
        "7": [],
        "8": [],
        "9": []
]

// input columns
file.withReader { reader ->
    while (noOfLines < 8) {
        line = reader.readLine()
        if (line != null) {
            if (line.charAt(1) != ' ') {
                columns['1'] << line.charAt(1)
            }
            if (line.charAt(5) != ' ') {
                columns['2'] << line.charAt(5)
            }
            if (line.charAt(9) != ' ') {
                columns['3'] << line.charAt(9)
            }
            if (line.charAt(13) != ' ') {
                columns['4'] << line.charAt(13)
            }
            if (line.charAt(17) != ' ') {
                columns['5'] << line.charAt(17)
            }
            if (line.charAt(21) != ' ') {
                columns['6'] << line.charAt(21)
            }
            if (line.charAt(25) != ' ') {
                columns['7'] << line.charAt(25)
            }
            if (line.charAt(29) != ' ') {
                columns['8'] << line.charAt(29)
            }
            if (line.charAt(33) != ' ') {
                columns['9'] << line.charAt(33)
            }
        }
        noOfLines++
    }

}
println("columns = $columns")
noOfLines = 0

file.withReader { reader ->
    while ((line = reader.readLine()) != null) {

        if (line.startsWith('move')) {
            println("line = $line")
            def split = line.split(' ')
            def nbrOfCrates = split[1] as Integer
            def columnSource = split[3]
            def columntarget = split[5]
            println("nbrOfCrates = $nbrOfCrates")
            println("columnSource = $columnSource")
            println("columntarget = $columntarget")
            println("BEFORE columns[columnSource] = ${columns[columnSource]}")
            println("BEFORE columns[columntarget] = ${columns[columntarget]}")
            def temp = []
            for (i in 0..(nbrOfCrates-1)) {
                def theCrate = columns[columnSource].remove(0)
                temp << theCrate
            }
            println("temp = $temp")
            def size = temp.size()-1
            println("size = $size")

            addElems(size, temp, columns, columntarget)

            println("AFTER columns[columnSource] = ${columns[columnSource]}")
            println("AFTER columns[columntarget] = ${columns[columntarget]}")
        }
        noOfLines++
    }

}

def addElems(int size, ArrayList temp, LinkedHashMap<String, ArrayList> columns, columntarget) {
    println("addElems size = ${size}, temp = $temp, columns = $columns, columntarget = $columntarget")
    def revListr = temp.reverse()
    println("revListr = $revListr")
    revListr.each { e ->
        columns[columntarget].add(0, e)
    }
}

def result = "${columns['1'].pop()}${columns['2'].pop()}${columns['3'].pop()}${columns['4'].pop()}${columns['5'].pop()}${columns['6'].pop()}${columns['7'].pop()}${columns['8'].pop()}${columns['9'].pop()}"
println "result ${result}"
