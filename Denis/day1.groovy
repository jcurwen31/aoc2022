File file = new File("puzzle_day1_1")
def line, noOfLines = 0;
def totalCal = 0
def bestTotalCal = 0
def bestTotalCals = new ArrayList<Integer>()

file.withReader { reader ->
    while ((line = reader.readLine()) != null) {
        def cal = line.size() == 0 ? "" : line as Integer
        if (cal != "") {
            totalCal += cal
        } else {
            if (totalCal > bestTotalCal) {
                bestTotalCal = totalCal
            }
            bestTotalCals << totalCal
            totalCal = 0
        }
        println "${line}"
        println "${cal}"
        noOfLines++
    }
    bestTotalCals.sort().reverse()

}
println "Nbr lines ${noOfLines}"
println "bestTotalCal ${bestTotalCal}"
println "bestTotalCal1 ${bestTotalCals.get(bestTotalCals.size() -1)}"
println "bestTotalCal2 ${bestTotalCals.get(bestTotalCals.size() -2)}"
println "bestTotalCal3 ${bestTotalCals.get(bestTotalCals.size() -3)}"
println "bestTotalCal add ${bestTotalCals.get(bestTotalCals.size() -1) + bestTotalCals.get(bestTotalCals.size() -2) + bestTotalCals.get(bestTotalCals.size() -3)}"
