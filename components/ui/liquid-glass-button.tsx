"use client"

import * as React from "react"
import { cn } from "@/lib/utils"

export interface LiquidGlassButtonProps
  extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  children?: React.ReactNode
}

export const LiquidGlassButton = React.forwardRef<
  HTMLButtonElement,
  LiquidGlassButtonProps
>(({ className, children, ...props }, ref) => {
  return (
    <button
      ref={ref}
      className={cn(
        "relative inline-flex items-center justify-center gap-2 rounded-full px-6 py-3 font-semibold text-white shadow-lg transition-all duration-300 hover:scale-[1.02] active:scale-[0.98]",
        "bg-white/10 backdrop-blur-md border border-white/20 hover:bg-white/20 hover:border-white/40",
        className
      )}
      {...props}
    >
      {children}
    </button>
  )
})

LiquidGlassButton.displayName = "LiquidGlassButton"

export default LiquidGlassButton
