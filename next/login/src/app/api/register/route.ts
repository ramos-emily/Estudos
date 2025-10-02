import { NextResponse } from "next/server";
import { db } from "@/db/drizzle";
import { users } from "@/db/schema";
import bcrypt from "bcryptjs";

export async function POST(req:Request) {
    const body = await req.json();
    const { username, password } = body;

    if (!username || !password){
        return NextResponse.json({ error: "Dados inválidos"}, { status: 400});
    }

    const hashedPassword = await bcrypt.hash(password, 10);

    try {
        await db.insert(users).values({
        username,
        password: hashedPassword,
        });

        return NextResponse.json({ success: true });
    } catch (err) {
        return NextResponse.json({ error: "Usuário já existe" }, { status: 400 });
    }
}