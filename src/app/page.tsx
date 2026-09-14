"use client";

import { useState } from "react";
import Image from "next/image";
import BookingWizard from "@/components/booking/BookingWizard";

export default function Home() {
  const [showBooking, setShowBooking] = useState(false);

  // Jika tombol booking di klik, langsung ganti tampilan ke Booking Wizard
  if (showBooking) {
    return (
      <div className="min-h-screen bg-paper flex flex-col items-center pt-8 px-4 pb-12 animate-in fade-in zoom-in-95 duration-300">
        <button 
          onClick={() => setShowBooking(false)} 
          className="self-start mb-6 text-dark font-bold text-[10px] uppercase tracking-widest flex items-center gap-2 hover:text-namata-pink transition-colors"
        >
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="m15 18-6-6 6-6"/></svg>
          Kembali
        </button>
        <div className="w-full max-w-[400px]">
          <div className="mb-8 text-center">
            <h2 className="font-editorial text-4xl font-bold text-dark mb-2">Reservation.</h2>
            <p className="text-[10px] uppercase tracking-widest text-dark/70">Pilih artist & jadwal</p>
          </div>
          <div className="bg-white border border-dark">
            <BookingWizard />
          </div>
        </div>
      </div>
    );
  }

  // Tampilan utama Link-in-Bio ala Memoji Studio
  return (
    <div className="min-h-screen bg-paper text-dark flex flex-col items-center justify-between py-12 px-6 animate-in fade-in duration-500">
      
      {/* Top / Brand */}
      <div className="flex flex-col items-center mt-8 md:mt-16 text-center">
        {/* Optional Logo Circle */}
        <div className="w-24 h-24 rounded-full bg-namata-pink/20 border border-dark flex items-center justify-center mb-6 overflow-hidden relative">
           {/* You can replace this with an actual logo image */}
           <span className="font-editorial text-4xl italic text-namata-pink leading-none pt-2">N</span>
        </div>
        <h1 className="font-editorial text-5xl font-bold tracking-tight mb-1">namata</h1>
        <h2 className="font-editorial text-2xl italic text-namata-pink">studio</h2>
        
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
          className="w-full bg-dark text-paper rounded-[2rem] py-4 text-[11px] font-bold uppercase tracking-[0.2em] hover:bg-namata-pink hover:text-dark transition-colors shadow-lg"
        >
          Online Booking
        </button>
        
        <a 
          href="https://wa.me/62881036695165" 
          target="_blank" 
          rel="noreferrer" 
          className="w-full bg-transparent border border-dark text-dark rounded-[2rem] py-4 text-[11px] font-bold uppercase tracking-[0.2em] text-center hover:bg-dark hover:text-paper transition-colors"
        >
          WhatsApp
        </a>
        
        <a 
          href="#" 
          target="_blank" 
          rel="noreferrer" 
          className="w-full bg-transparent border border-dark text-dark rounded-[2rem] py-4 text-[11px] font-bold uppercase tracking-[0.2em] text-center hover:bg-dark hover:text-paper transition-colors"
        >
          Google Maps
        </a>
        
        <a 
          href="https://www.instagram.com/nanata.studio" 
          target="_blank" 
          rel="noreferrer" 
          className="w-full bg-transparent border border-dark text-dark rounded-[2rem] py-4 text-[11px] font-bold uppercase tracking-[0.2em] text-center hover:bg-dark hover:text-paper transition-colors"
        >
          Instagram
        </a>
        
        
      </div>

      {/* Footer text */}
      <div className="text-[9px] text-dark/40 uppercase tracking-widest mt-12">
        copyright &copy; 2026 namata studio
      </div>
    </div>
  );
}
