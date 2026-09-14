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
          className="self-start mb-6 text-slate-800 font-bold text-xs uppercase tracking-widest font-semibold flex items-center gap-2 hover:text-nanata-pink transition-colors"
        >
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="m15 18-6-6 6-6"/></svg>
          Kembali
        </button>
        <div className="w-full max-w-[400px]">
          <div className="mb-8 text-center">
            <h2 className="text-2xl font-bold text-slate-800 mb-2">Reservation.</h2>
            <p className="text-[10px] uppercase tracking-widest text-slate-800/70">Pilih artist & jadwal</p>
          </div>
          <div className="bg-white w-full shadow-xl rounded-xl overflow-hidden border border-dark/5">
            <BookingWizard />
          </div>
        </div>
      </div>
    );
  }

  // Tampilan utama Link-in-Bio ala Memoji Studio
  return (
    <div className="min-h-screen relative bg-[#FFF7F9] text-slate-800 flex flex-col items-center justify-between py-12 px-6 overflow-hidden">
      
      
      
      {/* Top / Brand */}
      <div className="flex flex-col items-center mt-4 md:mt-12 text-center z-10 w-full">
        <div className="relative w-32 h-32 mb-6 rounded-full overflow-hidden shadow-sm border-[3px] border-white">
           <Image src="/logo.jpg" alt="Nanata Studio Logo" fill className="object-cover" priority />
        </div>
        
        <div className="mt-4 flex flex-col items-center gap-2 text-xs text-slate-800/70 tracking-widest font-medium uppercase">
          <p className="font-semibold text-slate-800">Eyelash <span className="mx-2 text-nanata-pink">•</span> Nail Art <span className="mx-2 text-nanata-pink">•</span> Hair</p>
          <p className="text-xs text-slate-500 mt-2">Jl. Caman Raya No.11, Bekasi 17412</p>
          <p className="text-xs text-slate-500">Open 10.00 - 21.00 (Everyday)</p>
        </div>
      </div>

      {/* Buttons Container */}
      <div className="w-full max-w-[320px] flex flex-col gap-4 mt-8 mb-auto z-10">
        <button 
          onClick={() => setShowBooking(true)} 
          className="w-full bg-[#E8A0BF] text-white rounded-full py-4 text-xs font-bold uppercase tracking-widest hover:bg-[#d98bb0] transition-colors shadow-md"
        >
          Online Booking
        </button>
        
        <a 
          href="https://wa.me/6285283120151" 
          target="_blank" 
          rel="noreferrer" 
          className="w-full bg-white border border-[#E8A0BF]/20 text-slate-700 rounded-full py-4 text-xs font-bold uppercase tracking-widest text-center hover:border-[#E8A0BF] hover:text-[#E8A0BF] transition-colors shadow-sm"
        >
          WhatsApp
        </a>
        
        <a 
          href="https://maps.app.goo.gl/iuF843vMhZYGH1YG9" 
          target="_blank" 
          rel="noreferrer" 
          className="w-full bg-white border border-[#E8A0BF]/20 text-slate-700 rounded-full py-4 text-xs font-bold uppercase tracking-widest text-center hover:border-[#E8A0BF] hover:text-[#E8A0BF] transition-colors shadow-sm"
        >
          Google Maps
        </a>
        
        <a 
          href="https://www.instagram.com/nanata.studio" 
          target="_blank" 
          rel="noreferrer" 
          className="w-full bg-white border border-[#E8A0BF]/20 text-slate-700 rounded-full py-4 text-xs font-bold uppercase tracking-widest text-center hover:border-[#E8A0BF] hover:text-[#E8A0BF] transition-colors shadow-sm"
        >
          Instagram
        </a>
      </div>

      {/* Footer text */}
      <div className="text-[10px] text-slate-800/30 uppercase tracking-widest mt-12 z-10">
        copyright &copy; 2026 nanata studio
      </div>
    </div>
  );
}
