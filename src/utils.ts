
export function parseLine(line: string): string;
export function parseLine<T>(line: string, transform: (str: string) => T): T;
export function parseLine(line: string, transform?: (str: string) => unknown)  {
    if (transform) {
        return transform(line.trim())
    }

    return line.trim() || null
}
