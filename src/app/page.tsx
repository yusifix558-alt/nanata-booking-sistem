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
          <div className="bg-white w-full shadow-xl rounded-xl overflow-hidden border border-dark/5">
            <BookingWizard />
          </div>
        </div>
      </div>
    );
  }

  // Tampilan utama Link-in-Bio ala Memoji Studio
  return (
    <div className="min-h-screen relative bg-[#fdfcfb] text-dark flex flex-col items-center justify-between py-12 px-6 overflow-hidden">
      
      {/* Decorative Background Blobs */}
      <div className="absolute top-0 left-0 w-full h-full overflow-hidden -z-10 pointer-events-none">
        <div className="absolute top-[-5%] left-[-10%] w-[80%] h-[40%] rounded-full bg-nanata-pink/20 blur-3xl opacity-60"></div>
        <div className="absolute bottom-[-5%] right-[-10%] w-[80%] h-[40%] rounded-full bg-teal-100/40 blur-3xl opacity-60"></div>
      </div>
      
      {/* Top / Brand */}
      <div className="flex flex-col items-center mt-4 md:mt-12 text-center z-10 w-full">
        <div className="relative w-44 h-44 mb-2">
           <Image src="/logo.jpg" alt="Nanata Studio Logo" fill className="object-contain mix-blend-multiply" priority />
        </div>
        
        <div className="mt-4 flex flex-col items-center gap-2 text-xs text-dark/70 tracking-widest font-medium uppercase">
          <p className="font-semibold text-dark">Eyelash <span className="mx-2 text-nanata-pink">•</span> Nail Art <span className="mx-2 text-nanata-pink">•</span> Hair</p>
          <p className="text-[10px] opacity-80 mt-1">Jl. Caman Raya No.11, Bekasi 17412</p>
          <p className="text-[10px] opacity-80">Open 10.00 - 21.00 (Everyday)</p>
        </div>
      </div>

      {/* Buttons Container */}
      <div className="w-full max-w-[320px] flex flex-col gap-3.5 mt-10 mb-auto z-10">
        <button 
          onClick={() => setShowBooking(true)} 
          className="w-full bg-dark text-paper rounded-2xl py-4 text-xs font-bold uppercase tracking-widest hover:bg-nanata-pink hover:text-dark transition-all shadow-lg hover:shadow-xl hover:-translate-y-0.5"
        >
          Online Booking
        </button>
        
        <a 
          href="https://wa.me/6285283120151" 
          target="_blank" 
          rel="noreferrer" 
          className="w-full bg-white/70 backdrop-blur-md border border-dark/10 text-dark rounded-2xl py-4 text-xs font-semibold uppercase tracking-widest text-center hover:bg-white hover:border-dark/30 transition-all shadow-sm hover:shadow-md"
        >
          WhatsApp
        </a>
        
        <a 
          href="https://maps.app.goo.gl/iuF843vMhZYGH1YG9" 
          target="_blank" 
          rel="noreferrer" 
          className="w-full bg-white/70 backdrop-blur-md border border-dark/10 text-dark rounded-2xl py-4 text-xs font-semibold uppercase tracking-widest text-center hover:bg-white hover:border-dark/30 transition-all shadow-sm hover:shadow-md"
        >
          Google Maps
        </a>
        
        <a 
          href="https://www.instagram.com/nanata.studio" 
          target="_blank" 
          rel="noreferrer" 
          className="w-full bg-white/70 backdrop-blur-md border border-dark/10 text-dark rounded-2xl py-4 text-xs font-semibold uppercase tracking-widest text-center hover:bg-white hover:border-dark/30 transition-all shadow-sm hover:shadow-md"
        >
          Instagram
        </a>
      </div>

      {/* Footer text */}
      <div className="text-[10px] text-dark/30 uppercase tracking-widest mt-12 z-10">
        copyright &copy; 2026 nanata studio
      </div>
    </div>
  );
}
