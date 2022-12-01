import * as path from "path";
import * as fs from "fs";
import * as math from 'mathjs'
import { parseLine } from "../utils";
const dir = path.join(__dirname);

const SPLITTER = "\n"
const input = fs.readFileSync(`${dir}/input.txt`, 'utf-8')
    .trim()
    .split(SPLITTER)
    .map((line, idx) => parseLine(line, Number) || null)

console.log("first 30 input:",input.slice(0, 30))
console.log("input length:", input.length)
// ***************************** ********************************
const _data = input
    .reduce<[Record<string, number[]>, number]>((acc, line, idx, arr) => {
        const [obj, i] = acc
        if (line) {
            obj[`${i}`] = [...obj[`${i}`], +line]
            return [obj, i]
        } else {
            obj[`${i+1}`] = []
            return [obj, i+1]
        }
    }, [{1: []}, 1] as [Record<string, number[]>, number])
const [data,] = _data
const sums = Object.values(data).map(vals => vals.reduce((sum, v) => sum + v, 0))
console.log("part 1", math.max(...sums))

sums.sort((a,b) => a > b ? -1 :1)
console.log("part 2",math.sum(...sums.slice(0,3)))
