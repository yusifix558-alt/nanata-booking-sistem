"use client";

import { useState } from "react";
import Image from "next/image";
import BookingWizard from "@/components/booking/BookingWizard";

export default function Home() {
  const [showBooking, setShowBooking] = useState(false);

  // Jika tombol booking di klik, langsung ganti tampilan ke Booking Wizard
  if (showBooking) {
    return (
      <div className="min-h-screen bg-paper flex flex-col items-center pt-8 px-4 pb-12 ">
        <button 
          onClick={() => setShowBooking(false)} 
          className="self-start mb-6 text-dark font-bold text-xs uppercase tracking-widest font-semibold flex items-center gap-2 hover:text-nanata-pink transition-colors"
        >
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="m15 18-6-6 6-6"/></svg>
          Kembali
        </button>
        <div className="w-full max-w-[400px]">
          <div className="mb-8 text-center">
            <h2 className="text-2xl font-bold text-dark mb-2">Reservation.</h2>
            <p className="text-[10px] uppercase tracking-widest text-dark/70">Pilih artist & jadwal</p>
          </div>
          <div className="bg-white w-full">
            <BookingWizard />
          </div>
        </div>
      </div>
    );
  }

  // Tampilan utama Link-in-Bio ala Memoji Studio
  return (
    <div className="min-h-screen bg-paper text-dark flex flex-col items-center justify-between py-12 px-6 ">
      
      {/* Top / Brand */}
      <div className="flex flex-col items-center mt-8 md:mt-16 text-center">
        <div className="relative w-36 h-36 md:w-48 md:h-48 mb-2">
           <Image src="/logo.jpg" alt="Nanata Studio Logo" fill className="object-contain mix-blend-multiply" priority />
        </div>
        
        <div className="mt-6 flex flex-col items-center gap-2 text-[11px] text-dark/80 tracking-wider font-medium">
          <p>Eyelash, Nail Art, Hair.</p>
          <p className="text-center">Jl. Caman Raya No.11, Bekasi 17412</p>
          <p>Open 10.00 AM - 21.00 PM (Everyday)</p>
        </div>
      </div>

      {/* Buttons Container */}
      <div className="w-full max-w-[320px] flex flex-col gap-4 mt-12 mb-auto">
        <button 
          onClick={() => setShowBooking(true)} 
          className="w-full bg-dark text-paper rounded-[2rem] py-4 text-xs font-semibold uppercase tracking-widest hover:bg-nanata-pink hover:text-dark transition-colors shadow-lg"
        >
          Online Booking
        </button>
        
        <a 
          href="https://wa.me/6285283120151" 
          target="_blank" 
          rel="noreferrer" 
          className="w-full bg-transparent border border-dark text-dark rounded-[2rem] py-4 text-xs font-semibold uppercase tracking-widest text-center hover:bg-dark hover:text-paper transition-colors"
        >
          WhatsApp
        </a>
        
        <a 
          href="https://maps.app.goo.gl/iuF843vMhZYGH1YG9" 
          target="_blank" 
          rel="noreferrer" 
          className="w-full bg-transparent border border-dark text-dark rounded-[2rem] py-4 text-xs font-semibold uppercase tracking-widest text-center hover:bg-dark hover:text-paper transition-colors"
        >
          Google Maps
        </a>
        
        <a 
          href="https://www.instagram.com/nanata.studio" 
          target="_blank" 
          rel="noreferrer" 
          className="w-full bg-transparent border border-dark text-dark rounded-[2rem] py-4 text-xs font-semibold uppercase tracking-widest text-center hover:bg-dark hover:text-paper transition-colors"
        >
          Instagram
        </a>
        
        
      </div>

      {/* Footer text */}
      <div className="text-[10px] text-dark/40 uppercase tracking-widest mt-12">
        copyright &copy; 2026 nanata studio
      </div>
    </div>
  );
}
