import type { Metadata } from "next";
import { Jost, Cormorant_Garamond } from "next/font/google";
import "./globals.css";


import SplashScreen from "@/components/SplashScreen";
import FloatingWhatsApp from "@/components/FloatingWhatsApp";

const fontSans = Jost({ subsets: ["latin"], variable: "--font-sans" });
const fontEditorial = Cormorant_Garamond({ subsets: ["latin"], weight: ["300", "400", "600", "700"], style: ["normal", "italic"], variable: "--font-editorial" });

export const viewport = {
  width: "device-width",
  initialScale: 1,
  maximumScale: 1,
  userScalable: false,
};

export const metadata: Metadata = {
  title: "Nanata Studio | Nail Art & Eyelash Extension",
  description: "Tingkatkan rasa percaya dirimu dengan sentuhan nail art premium dan treatment bulu mata dari ahlinya.",
  keywords: ["Nanata Studio", "Nail Art", "Eyelash Extension", "Beauty Studio"],
  openGraph: {
    title: "Nanata Studio | Nail Art & Eyelash Extension",
    description: "Tingkatkan rasa percaya dirimu dengan sentuhan nail art premium dan treatment bulu mata dari ahlinya.",
    url: "https://nanatastudio.id",
    siteName: "Nanata Studio",
    locale: "id_ID",
    type: "website",
  },
  robots: {
    index: true,
    follow: true,
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="id" className="scroll-smooth">
      <body className={`${fontSans.variable} ${fontEditorial.variable} font-sans bg-[#EAEAEA] text-dark antialiased selection:bg-nanata-pink selection:text-dark flex justify-center`}>
        <div className="w-full max-w-[430px] min-h-screen bg-paper relative shadow-2xl overflow-x-hidden border-x border-dark/10">
        <SplashScreen />
        
        <main className="min-h-screen">
          {children}
        </main>
        <FloatingWhatsApp />
        
        </div>
      </body>
    </html>
  );
}
