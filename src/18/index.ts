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


console.log("part 1", undefined)

console.log("part 2", undefined)
