import type { Metadata } from "next";
import { Jost, Cormorant_Garamond } from "next/font/google";
import "./globals.css";
import Header from "@/components/Header";
import Footer from "@/components/Footer";
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
  title: "Namata Studio | Nail Art & Eyelash Extension",
  description: "Tingkatkan rasa percaya dirimu dengan sentuhan nail art premium dan treatment bulu mata dari ahlinya.",
  keywords: ["Namata Studio", "Nail Art", "Eyelash Extension", "Beauty Studio"],
  openGraph: {
    title: "Namata Studio | Nail Art & Eyelash Extension",
    description: "Tingkatkan rasa percaya dirimu dengan sentuhan nail art premium dan treatment bulu mata dari ahlinya.",
    url: "https://namatastudio.id",
    siteName: "Namata Studio",
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
    <html lang="id" className="scroll-smooth overflow-x-hidden">
      <body className={`${fontSans.variable} ${fontEditorial.variable} font-sans bg-paper text-dark antialiased selection:bg-namata-pink selection:text-dark overflow-x-hidden`}>
        <SplashScreen />
        <Header />
        <main className="min-h-screen">
          {children}
        </main>
        <FloatingWhatsApp />
        <Footer />
      </body>
    </html>
  );
}
