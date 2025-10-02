import { NextResponse } from "next/server";
import { db } from "@/db/drizzle";
import { users } from "@/db/schema";
import bcrypt from "bcryptjs";
import { eq } from "drizzle-orm";

export async function POST(req: Request) {
  const body = await req.json();
  const { username, password } = body;

  if (!username || !password) {
    return NextResponse.json({ error: "Dados inválidos" }, { status: 400 });
  }

  // procura usuário no banco
  const [user] = await db.select().from(users).where(eq(users.username, username));

  if (!user) {
    return NextResponse.json({ error: "Usuário não encontrado" }, { status: 401 });
  }

  // compara senha
  const valid = await bcrypt.compare(password, user.password);

  if (!valid) {
    return NextResponse.json({ error: "Senha incorreta" }, { status: 401 });
  }

  // aqui poderia gerar JWT ou cookie de sessão
  return NextResponse.json({ success: true, user: { id: user.id, username: user.username } });
}
