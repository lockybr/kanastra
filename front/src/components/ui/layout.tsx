import { ReactElement, ReactNode } from "react";

type LayoutProps = {
  children: ReactNode
}

function Layout({ children }: LayoutProps): ReactElement {
  return (
    <main className="p-6 flex flex-col gap-8 h-screen">
      { children }
    </main>
  );
}

export { Layout };
